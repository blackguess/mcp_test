# import lmstudio as lms
# model = lms.llm("qwen2-vl-2b-instruct")
# image_path = "G:/asset/udWJrbivRr.jpg" # Replace with the path to your image
# image_handle = lms.prepare_image(image_path)
# chat = lms.Chat()
# chat.add_user_message("Describe this image please", images=[image_handle])
# prediction = model.respond(chat)
# print(prediction)

s = '<think>Okay, so I got a message saying "hi". The user is greeting me but hasn\'t provided any specific questions or requests yet.\n\nI need to decide whether to use the available tool here. Looking at the tools provided, there\'s only one called "fetch" which fetches a website\'s content based on a URL. But since the user just said "hi", I don\'t have enough information to know if they want me to access any URLs or web content.\n\nI should probably respond directly without using the tool because no action is needed yet. So, my response will be friendly and let them know how they can ask for help with their specific needs.</think>\n\n{"tool": "none", "response": "Hello! How can I assist you today?"}'
import re
p = re.compile(r'<think>\n.*\n</think>\n\n')
print(p.search(s))
s2 = '<think>saa</think>'
# print(re.compile(r'<think>[]*</think>').search(s2))
start = s.find('<think>')
start = s.find('</think>')
s = s[start+8:].strip()
print(s.strip())
import json
response = json.loads(s)
print(response)