class myerror(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
def say_nick(nick):
    if nick == "바보":
        raise myerror()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except myerror as e:
    print(e)