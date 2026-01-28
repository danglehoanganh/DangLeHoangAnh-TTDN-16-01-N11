<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Development of an Asset and Accounting Management System for Enterprises (DaiNam University)
    </a>
</h2>
<h2 align="center">
  Thiết kế và triển khai hệ thống quản lý tài sản và kế toán doanh nghiệp bằng Odoo
</h2>
<div align="center">
    <p align="center">
        <img src="aiotlab_logo (1).png" alt="AIoTLab Logo" width="170"/>
        <img src="fitdnu_logo (1).png" alt="AIoTLab Logo" width="180"/>
        <img src="dnu_logo (1).png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)

</div>

### Hệ điều hành
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
### Công nghệ chính
[![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![XML](https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=codeforces&logoColor=white)](https://www.w3.org/XML/)
### Cơ sở dữ liệu
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
</div>



## 👥 Thành viên nhóm 11

| No. | Name          |
|-----|---------------|
| 1   | Đặng Lê Hoàng Anh  |
| 2   | Mai Đức Hòa    |
| 3   | Nguyễn Khôi Nguyên      |


# 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

## 1.1. Clone project.
git clone https://github.com/danglehoanganh/DangLeHoangAnh-TTDN-16-01-N11.git
git checkout 

## 1.2. cài đặt các thư viện cần thiết

Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết

```
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
```
## 1.3. khởi tạo môi trường ảo.

`python3.10 -m venv ./venv`
Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu

```
source venv/bin/activate
pip3 install -r requirements.txt
```

# 2. Setup database

Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.

`sudo docker-compose up -d`

# 3. Setup tham số chạy cho hệ thống

## 3.1. Khởi tạo odoo.conf

Tạo tệp **odoo.conf** có nội dung như sau:

```
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5432
xmlrpc_port = 8069
```
Có thể kế thừa từ **odoo.conf.template**

Ngoài ra có thể thêm mổ số parameters như:

```
-c _<đường dẫn đến tệp odoo.conf>_
-u _<tên addons>_ giúp cập nhật addons đó trước khi khởi chạy
-d _<tên database>_ giúp chỉ rõ tên database được sử dụng
--dev=all giúp bật chế độ nhà phát triển 
```

# 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

Người sử dụng truy cập theo đường dẫn _http://localhost:8069/_ để đăng nhập vào hệ thống.

Hoàn tất
    
python3 odoo-bin.py -c odoo.conf -u all

# 5. Hình ảnh hệ thống

* Giao diện module nhân viên:

   <p align="center">
  <img src="Screenshot 2026-01-27 205038.png" alt="GitHub Logo" width="800">
</p>
<p align="center">Hình 1</p> 
Mô tả hệ thống:
 Tại giao diện module Nhân sự, hệ thống hiển thị danh sách nhân viên của doanh nghiệp.
Mỗi nhân viên được quản lý với các thông tin cơ bản như họ tên, chức vụ, phòng ban và thông tin liên hệ.
Module Nhân sự đóng vai trò nền tảng trong hệ thống, bởi nhân viên có thể được liên kết trực tiếp với tài sản trong quá trình sử dụng, bảo trì hoặc quản lý trách nhiệm tài sản.
Dữ liệu từ module Nhân sự được dùng để xác định người quản lý, người sử dụng tài sản, giúp nâng cao tính minh bạch và khả năng truy vết trong quá trình vận hành.


* Giao diện module quản lý tài sản:

   <p align="center">
  <img src="Screenshot 2026-01-27 145802.png" alt="GitHub Logo" width="800">
</p>
<p align="center">Hình 2</p> 
Mô tả hệ thống:
 Tại giao diện quản lý tài sản, hệ thống cho phép theo dõi danh sách các tài sản hiện có trong doanh nghiệp.
Mỗi tài sản bao gồm các thông tin như mã tài sản, tên tài sản, loại tài sản, giá trị, ngày mua, tình trạng và vị trí sử dụng.
Hệ thống hỗ trợ phân loại tài sản theo từng nhóm như thiết bị hoặc vật tư, đồng thời cho phép lọc nhanh theo tình trạng sử dụng.
Ngoài ra, người dùng có thể đính kèm hình ảnh để tăng khả năng nhận diện và quản lý trực quan.
Thông tin tài sản được lưu trữ tập trung và sẵn sàng liên kết với các nghiệp vụ tài chính – kế toán liên quan.

* Giao diện module quản lý tài chính?kế toán:

   <p align="center">
  <img src="Screenshot 2026-01-27 154008.png" alt="GitHub Logo" width="800">
</p>
<p align="center">Hình 3</p> 
Mô tả hệ thống: 
Trong module Tài chính – Kế toán, hệ thống quản lý các nghiệp vụ thu và chi phát sinh liên quan đến tài sản.
Tại giao diện quản lý, các chứng từ kế toán được hiển thị theo ngày, loại giao dịch, số tiền và trạng thái xử lý.
Các khoản chi như mua sắm, bảo trì tài sản sẽ được ghi nhận trực tiếp vào hệ thống kế toán.
Dữ liệu này có thể được sử dụng để tổng hợp báo cáo tài chính, theo dõi chi phí và phục vụ công tác quản trị doanh nghiệp.
Việc tích hợp giữa quản lý tài sản và kế toán giúp giảm thiểu nhập liệu thủ công, đồng thời đảm bảo tính nhất quán của dữ liệu.

## Kết luận

Đề tài đã tập trung thiết kế và triển khai một hệ thống quản lý tài sản và kế toán doanh nghiệp nhằm hỗ trợ tự động hóa các nghiệp vụ quản lý tài sản, ghi nhận kế toán và tổng hợp dữ liệu tài chính. Thông qua việc xây dựng các mô-đun chức năng rõ ràng, hệ thống giúp nâng cao tính chính xác, minh bạch và hiệu quả trong quá trình quản lý.
Kết quả đạt được cho thấy hệ thống có khả năng đáp ứng các yêu cầu cơ bản của doanh nghiệp, đồng thời tạo nền tảng để mở rộng và tích hợp thêm các chức năng nâng cao trong tương lai như báo cáo phân tích, phân quyền chi tiết và kết nối với các hệ thống quản trị khác. Đây là tiền đề quan trọng để ứng dụng hệ thống vào thực tiễn quản lý doanh nghiệp.





