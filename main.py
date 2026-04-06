from read_pdf import read_pdf
from answer_question import answer_question

context = read_pdf('sample.pdf')
question = input("Please enter your question: ")
answer = answer_question(context, question)
print(answer)