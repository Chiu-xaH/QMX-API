# 得到sign
import execjs

def get_sign(data):
    # 通过调用逆向得到的JS代码生成sign
    #current_dir = os.path.dirname(__file__)
    js_file_path = "main.js"
    #os.path.join(current_dir, 'getSign', 'main.js')
    with open(js_file_path, 'r', encoding='utf-8') as f:
        js_code = f.read()

    ctx = execjs.get("Node").compile(js_code)
    sign = ctx.call("get_sign",data)
    return sign