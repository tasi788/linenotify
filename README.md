# Simple Line Notify Wrapper

## TODO
 - oauth flow

## Use
pass token in to `line` class  
`line = line(123123123123123)`

 - ### send_message
    ```python
    line.send_message(text='hello')
    # 1000 characters max
    ```  
    #### argument: 
     > text
      - `str` - **require**
 - ### send_photo
    ```python
    # from local file
    line.send_photo('hello.png', text='AQI Chart')
    # file size should be <= 3mb
    # accpet .png & .jpg

    # from url
    line.send_photo('http://exmaple.com/hello.jpg')
    # file size should be <= 3mb
    # only accpet .jpg
    ```
    #### argument: 
     > text
      - `str` - **require**, default by `'傳送圖片'`
     > photo
      - `(str | bytes)` - **require**
     > thumbnail
      - `str` - **option** default by an loading jpg
    