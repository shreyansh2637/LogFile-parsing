print('''
╭━━━┳╮╱╭┳━━━┳━━━┳╮╱╱╭┳━━━┳━╮╱╭┳━━━┳╮╱╭╮
┃╭━╮┃┃╱┃┃╭━╮┃╭━━┫╰╮╭╯┃╭━╮┃┃╰╮┃┃╭━╮┃┃╱┃┃
┃╰━━┫╰━╯┃╰━╯┃╰━━╋╮╰╯╭┫┃╱┃┃╭╮╰╯┃╰━━┫╰━╯┃
╰━━╮┃╭━╮┃╭╮╭┫╭━━╯╰╮╭╯┃╰━╯┃┃╰╮┃┣━━╮┃╭━╮┃
┃╰━╯┃┃╱┃┃┃┃╰┫╰━━╮╱┃┃╱┃╭━╮┃┃╱┃┃┃╰━╯┃┃╱┃┃
╰━━━┻╯╱╰┻╯╰━┻━━━╯╱╰╯╱╰╯╱╰┻╯╱╰━┻━━━┻╯╱╰╯''')
with open("log.txt","r") as f:
    lines=f.readlines()
o=open("output.text","wt")
print("IP\t\tDate/Time\t\t\tRequest\t\tProtocol/Version\tStatus code\tPacket size")
o.write("IP\t\tDate/Time\t\t\tRequest\t\tProtocol/Version\tStatus code\tPacket size\n\n")
for line in lines:
    line=line.replace('"',"")
    line=line.split(" ")
    y=line[0]
    for i in range(len(y),16):
        print(" ",end="")
    o.write(f"{line[0]}\t{line[3]+line[4]}\t{line[5]}\t\t{line[7]}\t\t{line[8]}\t\t{line[9]}\n")
    print(f"{line[0]}\t{line[3]+line[4]}\t{line[5]}\t\t{line[7]}\t\t{line[8]}\t\t{line[9]}")