# Database extra assignment
# Design Fulture order Car app
Reference: 
*) https://www.bmwusa.com/build-your-own.html?tl=grp-wdpl-bcom-mix-mn-.-nscf-.-.-#/studio/ewh8cz71/design  

*) https://www.bmwusa.com/build-your-own.html?tl=grp-wdpl-bcom-mix-mn-.-nscf-.-.-#/series  

Một số quy tắc chung:  
    +) Tất cả template dù với các vai trò khác nhau đều vẫn được dùng chung, vì quy tắc là controller chỉ cần gửi dữ liệu cho view, view đó sẽ tự biết render  
    +) Dữ liệu được gửi quy ước là data = {}, trong đó cần trường nào thì mình data["field1"] = ... Mục đích là để trong tương lai, mở rộng thêm nhiều trường dữ liệu cho vào view  
    +) Hàm trả về nên trả dưới dạng dictionary để dữ liệu cần lấy ở đầu ra chỉ cần 1 biến    
    +) Nếu có thể, dữ liệu các bạn lấy ra, hãy note nó ở phía sau hàm đó (giảm thời gian print và debug)  