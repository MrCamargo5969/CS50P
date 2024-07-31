x = input("File name: ").replace(" ", "").split(".")

if len(x) == 1:
    print("application/octet-stream")
elif len(x) == 3:
    print(f"application/{x[2]}")
else:
    match x[1]:
        case "png" | "gif":
            print(f"image/{x[1]}")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "pdf" | "PDF":
            print("application/pdf")
        case "zip":
            print(f"application/{x[1]}")
        case "txt":
            print(f"text/{x[0]}")
        case _:
            print("application/octet-stream")
