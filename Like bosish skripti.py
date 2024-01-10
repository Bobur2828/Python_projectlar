def like(a):
    if len(a)==0:
        print("Bu post hech kimga yoqmadi")
    elif len(a)==1:
        print(f"Bu {a[0]}ga yoqadi")
    elif len(a)==2:
        print(f"Bu {a[0]} va {a[1]} ga yoqadi")
    elif len(a)==3:
        print(f"Bu {a[0]}, {a[1]} va {a[2]} ga yoqadi")
    else:
        print(f"Bu {a[0]}, {a[1]} va yana {len(a)-2} kishiga yoqadi")

like(["Boburjon"])
like(["Boburjon","Azamjon"])
like(["Boburjon","Azamjon","Ikromjon"])
like(["Boburjon","Azamjon","Ikromjon","Murodjon","Toxirbek"])
