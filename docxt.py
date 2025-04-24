from docxtpl import DocxTemplate
teststr = "тестовый тесть"
doc = DocxTemplate("шаблон.docx")
context = { 'test' : ''+ teststr +'' ,
            'test2' : "Сучка хвост крючком",
            'test3' : "Жучка хвост пятачком",}
doc.render(context)
doc.save("шаблон-final.docx")