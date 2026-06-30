./main.sh
# hello world


from textnode import TextNode, TextType

def main():
    node = TextNode("some text", TextType.LINK, "https://www.example.com")
    print(node)

main()
