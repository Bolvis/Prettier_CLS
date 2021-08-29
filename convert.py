# SYNTAX: python convert.py <file name>
import sys

f = ""
new_f = ""

try:
    f = open(sys.argv[1])
    new_f = open(sys.argv[1].split(".")[0] + "_new.cls", "w")
except IndexError:
    print("You have to specify filename")
    exit(1)


body = f.read().replace("    ", "\t")
body = body.replace("> ", ">")
body = body.replace(">", "> ")
body = body.replace("> (", ">(")
body = body.replace("> >", ">>")
body = body.replace(", ", ",")
body = body.replace(",", ", ")
body = body.replace("string ", "String ")
body = body.replace("set<", "Set<")
body = body.replace("set <", "Set<")
body = body.replace("list <", "List<")
body = body.replace("list<", "List<")
body = body.replace("test", "Test")
body = body.replace("@istest", "@isTest")
body = body.replace("select", "SELECT")
body = body.replace("from", "FROM")
body = body.replace("where", "WHERE")
body = body.replace("If", "if")
body = body.replace("for(", "for (")
body = body.replace("if(", "if (")
body = body.replace("){", ") {")
body = body.replace(")\n\t{", ") {")
body = body.replace(")\n\t\t{", ") {")
body = body.replace(")\n\t\t\t{", ") {")
body = body.replace(")\n\t\t\t\t{", ") {")
body = body.replace(")\n\t\t\t\t\t{", ") {")
body = body.replace(")\n\t\t\t\t\t\t{", ") {")
body = body.replace("static TestMethod", "@isTest\n\tstatic")

new_f.write(body)
