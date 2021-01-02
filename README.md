# 2021서울하드웨어해커톤 IGLODD팀의 저장소
## 팀이름
IGLODD

## 작품명
허공터치 & 높이조절 키오스크

여기 키오스크 동작 움짤추가

## 작품개요 및 제작동기
언택트시대 속에서 코로나 감염의 위험으로 많은 자영업자 분들이 손님이 줄어들어 어려움을 겪고 있습니다.
키오스크의 터치스크린을 만질 때 바이러스 감염의 위험이 있기 때문에 이 문제를 해소하여 자영업자 분들을 돕고자 비접촉식 터치가 가능한 키오스크를 제작하였습니다.

비접촉식 터치에도 불구하고 키오스크의 화면까지 키가 닿지 않는 어린이들은 여전히 바이러스의 위험에 노출됩니다.
따라서 키오스크 화면의 높이를 조절하는 기능을 추가하였습니다.

![Notes_210103_022913](https://user-images.githubusercontent.com/60468060/103462922-03c54a00-4d6c-11eb-8035-da2f52e90614.jpg)

모니터에는 상품을 선택, 결제할 수 있는 GUI가 탑재되어 결제시 AWS IoT서버로 업로드 됩니다.
2D라이다가 모니터 앞의 영역을 스캔하여 손가락의 위치를 알아냅니다.
좌우에 스텝모터가 구동하는 리니어 레일 액추에이터가 부착되어 키오스크 화면을 위/아래(적외선센서의 값에 따라 결정)로 움직입니다.

## 팀원소개 및 역할분담
여기 팀원사진추가

이영: 팀장, 충북대학교 전자공학부 3학년, 라이다를 이용한 손가락 인식프로그램 개발

전상현: 충북대학교 전자공학부 3학년, HW 설계

이준기: 충북대학교 전자공학부 2학년, step모터 구동 펌웨어 개발

김동욱: 충북대학교 전자공학부 2학년, 키오스크 GUI프로그램 개발, 적외선 센서 펌웨어 개발

## 시스템 구성도
![시스템구성도](https://user-images.githubusercontent.com/60468060/103454535-81676680-4d28-11eb-9f01-d4409b5699af.png)

## 추가정보
### 사용부품
2DLidar : RPLIDAR A1 (43000원)

스텝모터드라이버 : AM_CS2P

스텝모터 : 17HD2049-4N

외관 : 합판, MDF

적외선센서 : SHARP 2YA021

### SW정보
B-L4S5I-IOT01A(stm32보드)개발환경 : STM32CubeIDE

라즈베리파이4 OS : 라즈비안 버스터 arm64

IoT서버 : AWS IoT Core

2DLidar개발환경 : ROS-Melodic(오픈소스 패키지: PCL, rplidar_ros(디바이스 드라이버))

GUI프로그램 라이브러리 : Tkinter

마우스 이동, 클릭 : pyautogui

CubeAI사용여부 : X

## 기존제품과의 비교
자료조사 결과 동일한 주제의 제품이 미국 GTT사(http://gtt.co.kr/en/biz/untacttouch.php )에 존재합니다.
이것은 디스플레이 제품으로 많은 수의 적외선레이저센서를 x, y축으로 빽빽히 설치한 모듈과 디스플레이가 결합되어 있습니다.
이 제품의 문제점은 많은 수의 센서가 사용되어 비용의 문제가 있는 것과 키오스크의 기존 디스플레이를 이 디스플레이 제품으로 교체해야한다는 것입니다.

저희 IGLODD팀이 제작한 허공터치의 경우 5~10만원의 저렴한 가격으로 구입이 가능한 2D라이다 센서하나만 있으면 디스플레이의 교체없이 구현가능하다는 큰 장점이 있습니다.

## 프로젝트 히스토리
### 2020-12-02
서울하드웨어해커톤 참가 결정

### 2020-12-04
주제결정을 위한 회의


주제후보

1. 독거노인을 위한 위험상황 발생알림 서비스(움직임탐지)

2. 허공터치 + 높이조절 키오스크


주제후보 중에서 2안으로 주제를 결정.

서울하드뒈어해커톤 참가신청서 제출.

### 2020-12-07
충북대학교 3학년 전상현 팀에 합류.

### 2020-12-18
전인원 종강 개발시작.

### 2020-12-22
HW설계 종료.

### 2020-12-23
라즈비안과 ROS호환(ROS에서 제공하는 오픈소스 패키지 다운로드)에 문제가 발생.

->ubuntu_server18.04(arm64) + ubuntu마테GUI를 OS로 채택하여 문제를 해결하여 ROS-melodic설치.

### 2020-12-24
ubuntu_server18.04(arm64) + ubuntu마테GUI를 OS로 사용한 경우 펌웨어의 문제로 모니터 화면회전이 안되는 이슈발생.

->라즈비안 버스터(arm64)를 OS로 채택, 수동적인 방법으로 ROS 오픈소스 패키지 다운로드.


다운로드 받은 라이다 디바이스드라이버로 정보획득.


GUI프로그램 제작완료.

### 2020-12-26
PCL에서 제공하는 API를 사용하여 라이다가 수집한 data처리, 손가락위치를 판별완료.

### 2020-12-27
HAL라이브러리 writepin을 사용하여 핀상태를 하나하나 변경하여 스텝모터 구동시 버벅이는 이슈발생.

->GPIO의 ODR레지스터에 값을 직접 변경하여 문제를 해결.


판별한 손가락의 위치로 마우스를 이동, 클릭하는 프로그램 제작완료.

### 2020-12-28
스텝모터가 정지하였을 때 상이 풀리지 않고 고정되어 있는 문제발생.

->GPIO의 BRR레지스터에 값을 입력하여 상을 풀어주었음.


스텝모터 제어종료


주문한 자작나무, MDF가 도착하여 외관 제작 시작.

### 2020-12-29
적외선센서의 값을 ADC기능을 사용하여 받았음.


주문한 자작나무, MDF가 규격에 맞지 않아 조립이 되지 않는 문제가 발생.

->나무를 가공하여 문제를 해결.


키오스크에서 주문한 내역을 AWS-IoT에 업로드하는 기능을 추가.

### 2020-12-30
외관제작 진행.

### 2020-12-31
주문한 자작나무, MDF가 규격에 맞지 않는 문제가 다시발생.

->나무를 가공하여 문제를 해결.


짧은 작품소개영상 제작.

### 2021-01-01
외관을 제작을 완료하였으나 밸런스의 문제로 모니터블럭이 위아래로 움직이지 않는 문제 발생.

### 2021-01-02
추가 목제를 조달하여 밸런스를 잡는 기구부를 추가하여 어제 발생하였던 문제를 해결.

GUI에 메뉴를 선택하면 음성이 나오는 기능을 추가.-> 음성이 나오면 프로그램이 지연되는 현상으로 롤백.

하단에 팀로고를 새김.

stm32CubeMX에서 제공하는 USB_DEVICE기능을 사용하여 마우스 구현을 하려고 하였으나 1회의 마우스 이동으로 좌우, 상하 각각 127픽셀 이동이 한계이기 때문에 1920x1080해상도에 적용하기 어려움을 확인하고 파이썬 라이브러리 pyautogui를 이용하여 마우스 기능을 구현하였음.

작품제작 종료.
### 2021-01-03
발표자료 제작.

깃허브 정리.

