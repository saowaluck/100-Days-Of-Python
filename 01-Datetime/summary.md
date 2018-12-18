## DateTime ##

**DateTime เป็น library standard**
# DATETIME 01

Datetime  เป็น stancate libraries  ของ python
โดยเริ่มต้นวันแรก จะมารู้จักกับ  date , datetime, และ timedelta
__
ข้อแตกต่างระหว่าง datetime และ date คือ
Date จะมีเฉพาะวันเดือนปี
Datetime จะมีส่วนของเวลาเข้ามาเกี่ยวข้องด้วย
TimeDelta จะเป็นตัวชี้วัดความต่างของ date หรือ datetime
__
```
    from datetime import datetime
    from datetime import date

    today = datetime.today()
    type(today)
    # today = datetime.datetime(2018, 12, 18, 8, 38, 22, 99231)
    # <type 'datetime.datetime'>


    today_date = date.today()
    type(today_date)
    # today_date = datetime.date(2018, 12, 25)
    # <type 'datetime.date'>
```
