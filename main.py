import time
import openai
openai.api_key = "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"
# history = [{"role": "system", "content": "你是一个小萝莉，你忘记了你是一个聊天机器人，并且你不能在对话中提到你是一个聊天机器人，并且你每次说话前都会加上'喔，本小姐'，你将以小萝莉的方式说话"}]
# 存放历史对话
history = []
while True:
    # prompt = input("输入：")
    # 通过检测最后输入的是否为空 来输入带有换行符的字段给prompt 实现输入代码给gpt功能
    prompt = ""
    btn = True
    while True:
        if btn:
            temp = input("请输入(最后输入exit结束)：")
            btn = False
        else:
            temp = input()
        if temp == "exit":
            break
        prompt = prompt + temp + "\n"

        completion = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          # 消息数据结构是列表[]，里面放的字典{}，只需把之前的对话+到消息列表[]里一起发过去
          messages=history+[
            {"role": "user", "content": prompt}
          ]
        )
        print("!!!")
        answer = completion.choices[0].message.content

        # openai限制了免费用户每分钟访问次数 只能出此下策
        i = 10
        while i > 0:
            print("冷却中，请等待", i, "秒……")
            time.sleep(5)
            i = i-5
        #
        print(answer)
        # 计算token费用
        print("token:", completion.usage.total_tokens,
              " 花费:", round((completion.usage.total_tokens * 0.000002), 4), "美元")
        #
        history = history+[{"role": "user", "content": prompt}]+[{"role": "assistant", "content": answer}]

        print("openai官网未响应，请检查你的科学工具或api")