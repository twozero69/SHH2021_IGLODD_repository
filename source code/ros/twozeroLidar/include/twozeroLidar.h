#include <iostream>
#include <math.h>
#include <algorithm>

#include <sensor_msgs/LaserScan.h>
#include <tf/transform_listener.h>
#include <laser_geometry/laser_geometry.h>
#include <pcl_ros/point_cloud.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_types.h>    
#include <pcl/point_cloud.h>
#include <pcl/conversions.h>
#include <pcl_ros/transforms.h>
#include <pcl/filters/passthrough.h>
#include <sensor_msgs/LaserScan.h>

#include <std_msgs/Float32.h>
#include <std_msgs/Int32.h>
#include <sensor_msgs/PointCloud2.h>


#include <pcl/segmentation/extract_clusters.h>
#include <pcl/segmentation/sac_segmentation.h>
#include <pcl/sample_consensus/ransac.h>
#include <pcl/filters/extract_indices.h>

#include <pcl/filters/statistical_outlier_removal.h>

class LIDAR
{
private:
    //subscriber
    ros::NodeHandle node_;
    ros::Subscriber scan_sub_;
    laser_geometry::LaserProjection projector_;
    tf::TransformListener tfListener_;

    //publisher
    ros::Publisher result_pub_;
   

public:
    //생성자 서브스크라이버, 퍼블리셔 초기화
    LIDAR();

    //라이다 콜백함수(여기서 모든 처리를 진행)
    void scanCallback(const sensor_msgs::LaserScan::ConstPtr& scan);
};
