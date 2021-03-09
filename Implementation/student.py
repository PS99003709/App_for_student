# from ClassRoom import *
# from cosolidated_data import *
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# '''Student class that has all functions that a student needs'''


# class student:
#     '''Constructor of student class'''

#     def __init__(self, ps):
#         self.ps = ps

#     def getScore(self):
#         '''This method is used for getting the score'''
#         my_data = data_for_graph()
#         return my_data[self.ps]

#     def classAverage(self):
#         '''This is used to get average score'''
#         res = avg()
#         return res

#     def get_Graph(self):
#         '''This returns the specific graphs'''
#         return radar_graph(self.ps)


# '''Faculty class for faculty functions'''


# class faculty:
#     '''Constructor of faculty'''

#     def __init__(self, ps_list):
#         self.ps_list = ps_list
#     '''This is to return avg of the class'''

#     def getAvg(self):
#         return avg()
#     '''This is for getting top 5 students'''

#     def get_top_five(self):
#         return top_five(0)
#     '''This is to get bottom 5'''

#     def get_bottom_five(self):
#         return bottom_five(0)
#     '''This returns all graphs'''

#     def get_graph(self):
#         for i in range(0, 10):
#             print(radar_graph(self.ps_list[i]))
#     '''This is for getting mails'''

#     def get_mail(self):
#         mail_list = []
#         for i in range(0, 10):
#             mail_list.append(post_test.iloc[i, 3])
#         return mail_list
#     '''Automailer code'''

    def send_mail(self):
        li = []
        for j in range(0, 10):
            li.append(post_test.iloc[j, 3])
        li = ['ashish.pareek@ltts.com', 'lalit.bhardwaj@ltts.com', 'ashish.nayak@ltts.com', 'prashantsudhir.bagal@ltts.com', 'aakarsh.mehta@ltts.com',
              'yash.jhajharia@ltts.com', 'manzar.hussain@ltts.com', 'digendrakumar.sahu@ltts.com', 'ankitkumar.yadav@ltts.com', 'manu.nadar@ltts.com']
        for i in range(0, 10):
            ps = get_PS()

            for i in range(10):
                image1 = f'RMap_0_of_{ps[i]}.jpeg'
                image2 = f'RMap_1_of_{ps[i]}.jpeg'
                image3 = f'RMap_2_of_{ps[i]}.jpeg'
                image4 = f'RMap_3_of_{ps[i]}.jpeg'

                sender_email = 'learningcorporate7@gmail.com'
                sender_ePass = '99003708'
                length = len(li[i])
                X = li[i]
                receiver_email = X

                print(receiver_email)

                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_email
                message['Subject'] = 'Mail using python'

                mail_text = '''Hello,
                This is a simple mail. There is file attachments in the mail, The mail is sent using Python SMTP library.
                Thank You'''

                message.attach(MIMEText(mail_text, 'plain'))
                with open(image1, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())

                encoders.encode_base64(part)
                with open(image2, "rb") as attachment:
                    part1 = MIMEBase("application", "octet-stream")
                    part1.set_payload(attachment.read())

                encoders.encode_base64(part1)
                with open(image3, "rb") as attachment:
                    part2 = MIMEBase("application", "octet-stream")
                    part2.set_payload(attachment.read())

                encoders.encode_base64(part2)
                with open(image4, "rb") as attachment:
                    part3 = MIMEBase("application", "octet-stream")
                    part3.set_payload(attachment.read())
                encoders.encode_base64(part3)
                part.add_header('Content-Disposition',
                                "attachment; filename= %s" % image1)
                part1.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image2)
                part2.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image3)
                part3.add_header('Content-Disposition',
                                 "attachment; filename= %s" % image4)
                message.attach(part)
                message.attach(part1)
                message.attach(part2)
                message.attach(part3)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(sender_email, sender_ePass)
                text = message.as_string()
                s.sendmail(sender_email, receiver_email, text)
                s.quit()
                print('Mail Sent')
