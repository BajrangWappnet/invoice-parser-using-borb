import typing
from borb.pdf.document.document import Document
from borb.pdf.pdf import PDF
import re
import nltk



# New import
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction

def main():

    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open("Parser/data/lowes_bill_2.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])

    assert d is not None
    # print(type(d))
    # print(len(l.get_text_from_pdf(d)))

    data = []
    data_1 = []
   

    for i in range(len(l.get_text_from_pdf(d))):
        # print(i)
        # print("-"*50)
        # print(l.get_text_from_pdf(d)[i])
        # data.append(l.get_text_from_pdf(d)[i].replace("\n", "").lower())

        # print(l.get_text_from_pdf(d)[i].lower().replace("\n"," ").replace("\x"," ").split(" "))
        
        # data_1.append(re.split(', |-|_|!|\+',l.get_text_from_pdf(d)[i].lower() ))

        data_1.append(l.get_text_from_pdf(d)[i].lower().split("\n"))

    

    # print("-"*50)
    # print(data_1)
    # print("-"*50)


    """For tokenization of words in list """
    
    """for words in data_1[0]:
    #     for word in words:

    #         tokens = nltk.word_tokenize(word)
    #     data.append(tokens)
    # print(data)



    # for i in range(len(data)):
    #     print(i, end=" ")
    #     print(data[i])
        """
    
    def searching_word(order):
       

        for j in range(len(data_1)):

            for i in range(len(data_1[j])):


            # print(count)
            # count =+ 1
            # print(word)
                search = re.findall(order, data_1[j][i])
                if len(search) > 0:
                    # print(search,data_1[j][i])
                    return j , i 
                        
           

    # searching_word(input("enter the word: "))

    # print(data_1)
    def quantity_search(start , end):
        # data_1[start+1,end]

        # To find start start value
        start_init = searching_word(start)

        #To find end value 
        end_init = searching_word(end)


        return data_1[start_init[0]][start_init[1]+1:end_init[1]]

        # print(start_init, end_init)

    
    item_list = quantity_search(input("enter the start: ").lower(), input("enter the End: ").lower())

    for i in item_list:
        print(i, "hi")





if __name__ == "__main__":
    main()