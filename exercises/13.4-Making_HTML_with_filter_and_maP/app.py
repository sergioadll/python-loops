all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(color):
    if color["sexy"]:
        return color["label"]
def generate_li(color):
    aux=color["label"]
    return "<li>"+aux+"</li>"

filtered=(list(filter(filter_colors,all_colors)))
htmlgenerate =(list(map(generate_li,filtered)))
n=""
print(n.join(htmlgenerate))
