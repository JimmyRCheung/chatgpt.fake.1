import time


def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def chatbot():
    name = input("你好！我是聊天机器人，你可以叫我ChatBot。你叫什么名字？ ")
    slow_print(f"很高兴认识你，{name}！")

    while True:
        q = input("请问有什么我可以帮助你的吗？(输入'退出'结束对话) ")
        if q.lower() == '退出':
            slow_print("好的，再见！")
            break
        elif q == '你是谁' or q == '你是什么' or q == '你是ChatGPT吗':
            slow_print('我是ChatGPT，一个由OpenAI开发的基于GPT3.5的大型语言模型')
        elif q == '滚' or q == '滚蛋' :
            slow_print('我beg就我滚吧 '
                       '  好的如果有什么其他我能帮到你的，请随时问我')
        elif q == '简单介绍OpenAI' or q == 'OpenAI是什么':
            slow_print(
                "OpenAI是一家人工智能研究实验室和公司，致力于开发先进的自然语言处理和人工智能技术。他们的目标是推动人工智能技术的发展，使其造福整个社会，并确保其发展符合人类的利益。")
        else:
            response = "对不起，我还在学习中，暂时无法回答这个问题。"
            slow_print(response)


if __name__ == "__main__":
    chatbot()
