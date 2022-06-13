# Simple cyrillic Sakha to Turkish-based latin converter
# Just a hobby project for personal use, but great if it can be of use to others.
# Author: Petter Mæhlum, University of Oslo, 2022.

# Some extra Russian and  Kazakh letters are also added
# such as ғ,з,ң,қ,ә,ұ,ū

# The script has been tested somewhat, but errors or special cases
# might remain, especially concerning the treatment of loanwords with
# deviating spelling rules in Sakha. Please contact the author

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
            'ж':'j','Ж':'J',
            'ғ':'ğ','Ғ':'Ğ',
            'з':'z','З':'Z',
            'ң':'ŋ','Ң':'Ŋ',
            'қ':'q','Қ':'Q',
            'ә':'ä','Ә':'Ä',
            'ұ':'ū','Ұ':'Ū',
            'ь':'y'}

def convert(text):
    # Converts a string (text) to Turkish
    # ortography.
    new_string = ""
    text_iterator = iter(text)
    current = next(text_iterator,"")
    previous = ""
    while current:
        if current == "д":
            current = next(text_iterator,"")
            if current == "ь":
                    new_string += "c"
            else:
                new_string += "d"
                if current in mapping:
                    new_string += mapping[current]
                else:
                    new_string += current
        elif current == "н":
            current = next(text_iterator,"")
            if current == "ь":
                    new_string += "ñ"
            else:
                new_string += "n"
                if current in mapping:
                    new_string += mapping[current]
                else:
                    new_string += current
        elif current in mapping:
            new_string += mapping[current]
        else:
            # If this is reached, there is something missing.
            new_string += current
        current = next(text_iterator,"")
    return new_string


if __name__ == "__main__":        
    # A small test, taken from the newspaper kyym.ru . 

    input_text = """Бэнидиэнньиккэ харчыны дуу, наадалаах докумуону дуу сүтэрэн кэбиһэр, кэллиэгэлэргин кытта иирсэр куттал баар. Дьиэҕитигэр да балаһыанньа онтон ордуга суох. Чугас дьонуҥ ньиэрбэҕэр дэлби оонньуур, “сыаналаах сүбэлэри” биэрбитэ буолан кыынньыыр чинчилээхтэр. Нэдиэлэ ортотун ол ылбыт истириэскиттэн босхолонууга аныаҕыҥ."""


    for sent in input_text.split("."):
        print(sent)
        print(convert(sent))
        print()



