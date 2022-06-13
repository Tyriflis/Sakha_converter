# Simple cyrillic Sakha to Turkish-based latin converter
# Just a hobby project for personal use, but great if it can be of use to others.
# Author: Petter Mæhlum, University of Oslo, 2022.


inputt = """Бэнидиэнньиккэ харчыны дуу, наадалаах докумуону дуу сүтэрэн кэбиһэр, кэллиэгэлэргин кытта иирсэр куттал баар. Дьиэҕитигэр да балаһыанньа онтон ордуга суох. Чугас дьонуҥ ньиэрбэҕэр дэлби оонньуур, “сыаналаах сүбэлэри” биэрбитэ буолан кыынньыыр чинчилээхтэр. Нэдиэлэ ортотун ол ылбыт истириэскиттэн босхолонууга аныаҕыҥ. Нэдиэлэ бүтүүтэ иирсээн, кыыһырсыы эмиэ “төннөн” кэлиэхтэрэ. Табыллар күннэр – 12, 13.Үлэҥ боппуруостарыгар ылсарыҥ уолдьаспыт. Нэдиэлэ саҕаланыытыгар дьыалабыай актыыбынаһыҥ барыта үтүө түмүктэниэ. Арай, 12-с чыыһылаҕа үпкэ-харчыга сыһыаннаах тугу да гыныма. Бу – эн табыллыбат күнүҥ. Бу нэдиэлэҕэ саамай табыллар кэмиҥ – өрөбүллэр. Бу кэмҥэ эн тото сынньаныаҥ, күүс-күдэх ылыаҥ, интэриэһинэй көрсүһүүлэргэ сылдьыаҥ.

Табыллар күннэриҥ – 10, 11, 14, 15.Үлэҕэр ситиһии да, кыайтарыы да сиэттиһэ сылдьаллар. Бэнидиэнньиккэ араас инвестиция, саҥа дьыала арыйыытын туһунан толкуйдаабатаҕыҥ да ордук. Ити боппуруостарынан нэдиэлэ ортотугар дьарыктаннаххына – ситиһии аргыстаныаҥ. Нэдиэлэ иккис аҥаарын туохха да долгуйбакка холкутук атаар, туох да сонун син биир суох буолуо.Бэнидиэнньиккэ аһара ыһыллаҕас, дьалбаа-дьалаҕай буолан эрэйи көрүөҥ. Онон, суолталаах докумуону, харчыны сүтэрбэт курдук тэрин-дьаһан. Ол да гыннар, бука, тугу эрэ сүтэрэриҥ буолуо. Санаа баттыгар түспүккүн доҕотторуҥ, чугас дьонуҥ уоскутуохтара, бэттэх аҕалыахтара. Таарыйа, хантан эбии харчы буларгар сыаналаах сүбэлэри биэриэхтэрэ. Өрөбүллэргэ кыайыы эмиэ төннөн кэлиэ. Табыллар күннэрБу нэдиэлэҕэ ыйааһыннар бэйэлэрин эрэ буолбакка, тулалыыр дьоннорун олоҕор эмиэ үтүөнэн дьайыахтара, элбэх дьонноох-сэргэлээх сирдэргэ сылдьан чугас, интэриэһинэй доҕоттору булуохтара. Нэдиэлэ иккис аҥаарыгар өрдөөҕүттэн иитиэхтээбит ыра санааҕыт олоххо киириэн сөп. Өрөбүллэргэ маҕаһыыннарга сылдьан ону-маны атыылас. Ол матайдаабыт харчыҥ уон оччо буолан бэйэҕэр төннүөҕэ. Табыллар күннэр – 9, 12, 13."""


# Some extra Russian and  Kazakh letters are also addedғзңқәұū
mapping = {'а':'a','А':'A',
            'б':'b','Б':'B',
            'в':'v','В':'V',
            'г':'g','Г':'G',
            'д':'d','Д':'D',
            'е':'e','Е':'E',
            'и':'i','И':'İ',
            'й':'y','Й':'Y',
            'к':'k','К':'K',
            'л':'l','Л':'L',
            'м':'m','М':'M',
            'н':'n','Н':'N',
            'о':'o','О':'O',
            'п':'p','П':'P',
            'р':'r','Р':'R',
            'с':'s','С':'S',
            'т':'t','Т':'T',
            'у':'u','У':'U',
            'ф':'f','Ф':'F',
            'х':'x','Х':'X',
            'ц':'ts','Ц':'Ts',
            'ч':'ç','Ч':'Ç',
            'ы':'ı','Ы':'I',
            'э':'e','Э':'E',
            'я':'ya','Я':'Ya',
            'ҕ':'ğ','Ҕ':'Ğ',
            'ҥ':'ŋ','Ҥ':'Ŋ',
            'ү':'ü','Ү':'Ü',
            'һ':'h','Һ':'H',
            'ө':'ö','Ө':'Ö',
            'ш':'sh','Ш':'Sh',
            'ю':'yu','Ю':'Yu',
            'ж':'zh','Ж':'Zh',
            'ғ':'ğ','Ғ':'Ğ',
            'з':'z','З':'Z',
            'ң':'ŋ','Ң':'Ŋ',
            'қ':'q','Қ':'Q',
            'ә':'ä','Ә':'Ä',
            'ұ':'ū','Ұ':'Ū',
            'ь':'y'}


print("".upper())

sin = list(set(inputt))
sin.sort()
print(sin)

def convert(text):
    newstreng = ""
    titerator = iter(text)
    current = next(titerator,"")
    previous = ""
    while current:
        if current == "д":
            current = next(titerator,"")
            if current == "ь":
                    newstreng += "c"
            else:
                newstreng += "d"
                if current in mapping:
                    newstreng += mapping[current]
                else:
                    newstreng += current
        elif current == "н":
            current = next(titerator,"")
            if current == "ь":
                    newstreng += "ɲ"
            else:
                newstreng += "n"
                if current in mapping:
                    newstreng += mapping[current]
                else:
                    newstreng += current
        elif current in mapping:
            newstreng += mapping[current]
        else:
            #print(current,"CODE: {}".format(ord(current)), " is not in mapping")
            newstreng += current
        current = next(titerator,"")
    return newstreng
        
for sent in inputt.split("."):
    print(sent)
    print(convert(sent))
    print()