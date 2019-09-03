HEX_COLOURS = {"blueviolet": "#8a2be2", "brown": "#a52a2a", "coral": "#ff7f50"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for {} is {}".format(colour_name, HEX_COLOURS.get(colour_name)))
    colour_name = input("Enter a colour name: ")
