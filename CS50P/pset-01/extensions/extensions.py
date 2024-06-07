def main():
    file_name = (input("Enter: ")).strip().lower()

    if file_name.find(".") == -1:
        print("application/octet-stream")
        return
    
    ext = file_name[file_name.rfind(".") + 1:]

    match ext:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
