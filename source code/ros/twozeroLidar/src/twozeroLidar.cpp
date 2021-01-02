#include "twozeroLidar.h"

float dist=0.3;
float max_x=0.507+dist;
float max_y=0.143;

LIDAR::LIDAR()
{
    //서브스크라이버-2Dlidar의 rawdata읽음
    scan_sub_ = node_.subscribe<sensor_msgs::LaserScan> ("/scan",100, &LIDAR::scanCallback,this);

    //퍼블리셔-탐지된 클러스터의 중앙점을 퍼블리쉬
    result_pub_=node_.advertise<sensor_msgs::PointCloud2>("/twozeroLidar/result",100,false);
}

void LIDAR::scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan)
{
    //1. 데이터 읽어오기
    //laser_scan읽어와서 pointcloud2로 변환
    sensor_msgs::PointCloud2 rawCloud;
    projector_.transformLaserScanToPointCloud("laser",*scan,rawCloud,tfListener_);

    //pointcloud2를 pclpointcloud2::Ptr로 변환()  이후에 ROI지정을 위해서 변환필요
    pcl::PCLPointCloud2::Ptr pclCloud(new pcl::PCLPointCloud2 ());
    pcl_conversions::toPCL(rawCloud, *pclCloud);

    //2. 관심영역(ROI)설정-스크린크기와 거리에 맞추어 탐지영역 설정
    pcl::PassThrough<pcl::PCLPointCloud2> pass;

    //x +정면 -후면
    pass.setInputCloud(pclCloud);
    pass.setFilterFieldName("x");
    pass.setFilterLimits(-max_x, -0.2);

    pcl::PCLPointCloud2::Ptr ROICloud(new pcl::PCLPointCloud2 ());
    pass.filter(*ROICloud);

     //y +좌측 -우측
    pass.setInputCloud(ROICloud);
    pass.setFilterFieldName("y");
    pass.setFilterLimits(-max_y, max_y);
    
    pass.filter(*ROICloud);
    
    pcl::PointCloud<pcl::PointXYZI> touchedPoints;
    if(!ROICloud->data.empty()){
        //3. 클러스터링
        //pclpointcloud2를 pointxyzi로 변환
        pcl::PointCloud<pcl::PointXYZI>::Ptr XYZCloud(new pcl::PointCloud<pcl::PointXYZI>);
        pcl::fromPCLPointCloud2(*ROICloud, *XYZCloud);

        //KdTree선언
        pcl::search::KdTree<pcl::PointXYZI>::Ptr tree(new pcl::search::KdTree<pcl::PointXYZI>);
        tree->setInputCloud(XYZCloud);

        //vector선언
        std::vector<pcl::PointIndices> clusterIndices; // 군집화된 결과물의 Index 저장, 다중 군집화 객체는 cluster_indices[0] 순으로 저장 

        //euclidean clustering
        pcl::EuclideanClusterExtraction<pcl::PointXYZI> ec;
        ec.setInputCloud(XYZCloud);       // 입력   
        ec.setClusterTolerance(0.08);   //8cm이내면 이어진 물체로 인식
        ec.setMinClusterSize(1);     // 최소 포인트 수 
        ec.setMaxClusterSize(20);   // 최대 포인트 수
        ec.setSearchMethod(tree);      // 위에서 정의한 탐색 방법 지정 
        ec.extract(clusterIndices);   // 군집화 적용 

        //4. 클러스터 중심점 추출

        //하나의 덩어리를 구성하는 포인트들을 저장
        pcl::PointCloud<pcl::PointXYZI>* lumpCloud = new pcl::PointCloud<pcl::PointXYZI>[clusterIndices.size()];
        for(std::vector<pcl::PointIndices>::const_iterator it = clusterIndices.begin(); it!=clusterIndices.end(); ++it){    //cluster의 개수만큼
            pcl::PointXYZI pt_term;
            for(std::vector<int>::const_iterator pit = it->indices.begin(); pit != it->indices.end(); ++pit){   //cluster안의 점 개수 만큼
                pt_term=XYZCloud->points[*pit];
                break;
            }
            touchedPoints.push_back(pt_term);
        }
            
    }

    //5. 결과 publish
    sensor_msgs::PointCloud2 result;
    pcl::toROSMsg(touchedPoints, result);
    result.header.frame_id = "laser";
    result_pub_.publish(result);
}

int main(int argc, char **argv)
{
    ros::init(argc, argv, "LIDAR");

    LIDAR LDR;

    while(ros::ok())
    {
        ros::spinOnce();
    }
    return 0;
}
