from gmail import GMail, Message
from random import choice
from datetime import datetime, time
html_content = """
<h1 style="text-align: center;">Cộng h&ograve;a x&atilde; hội chủ nghĩa việt nam</h1>
<p style="text-align: center;">độc lập - tự do - hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: left;">em chào thầy <span style="color: #00ff00;">Tuấn anh đẹp trai</span></p>
<p style="text-align: left;">T&ecirc;n em l&agrave; <span style="color: #00ff00;">Phạm Minh Đức</span></p>
<p style="text-align: left;"><span style="color: #000000;">Do em bị {sickness} nên em xin thầy cho em nghỉ 1 buổi :(</span></p>
<p style="text-align: left;"><span style="color: #000000;"></span></p>
<p style="text-align: left;"><span style="color: #000000;">Minh Đức</span></p>
"""
reasons = ['đau bụng', 'ẩy chỉa', 'Ebola', 'đau tay', 'đến ngày dâu' ]
reason = choice(reasons)
html_to_send = html_content.replace('{sickness}', reason)
gmail = GMail('tuananhc4e16@gmail.com', '01662518199')
msg = Message('Hello c4e', to= 'techkidsc4e16@gmail.com', html= html_to_send)

#gui mail vao 1 khung gio nhat dinh
while True:
    time_now = datetime.now().time().hour
    if time_now == 7:
        gmail.send(msg)
    break
