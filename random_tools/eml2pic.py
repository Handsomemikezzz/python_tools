import extract_msg
import email
from email import policy
from email.parser import BytesParser
import eml_parser
import pdfkit
eml_file_path = r'file_path'
out_pdf_path = r'pdf_path'
html_file_path=r'html_path'

def eml_to_html(eml_file_path):
    file_extension = eml_file_path.split('.')[-1].lower()
    if file_extension =='eml':
        with open(eml_file_path,'rb') as f:
            a = f.read()
        eml = eml_parser.eml_parser.decode_email_b(a,True,False)
        if len(eml['body'])>1:
            html_content =eml['body'][1]['content']
        else:
            html_content =eml['body'][0]['content']
        return html_content
    if file_extension =='msg':
        msg = extract_msg.openMsg(eml_file_path)
        html_content=msg.htmlBody.edcode('utf-8')
        return html_content

#转为html代码
html_code = eml_to_html(eml_file_path)

#存为html文件
try:
    with open(html_file_path,'w',encoding='gb2312') as html_file:
        html_file.write(html_code)
except UnicodeEncodeError as e:
    print('部分字符无法解析')
    pass
print('finish')
try:
    pdfkit.from_file(html_file_path,out_pdf_path,options={'encoding':'gb2312','enable-local-file-access':True})
except:
    print('邮件中存在网址')#针对内网网址外网无法访问
    pass
#path_wk= r‘wkhtmltopdf安装路径’
#config =pdfkit.configuration(wkhtmltopdf = path_wk)    若找不到配置，则用这两行，在在pdfkit函数中指定config为config即可
