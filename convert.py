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
except FileNotFoundError:
    print("File does not exist: " + sys.argv[1])
    exit(1)


def fix_operators(text, operator, operator_name):
    text = text.replace(operator, operator_name)
    text = text.replace(operator_name + " ", operator_name)
    text = text.replace(" " + operator_name, operator_name)
    text = text.replace(" " + operator_name + " ", operator_name)
    text = text.replace(operator_name, " " + operator_name + " ")
    return text


body = f.read().replace("    ", "\t")  # change 4 spaces to one tab
f.close()
body = body.replace("   ", "\t")  # change 3 spaces to one tab to fix spacing
body = body.replace("  ", "")  # remove all 2 spaces symbols to fix spacing
body = body.replace("//", "COMMENT_DASH_DASH")
body = body.replace("/*", "COMMENT_DASH_STAR")
body = body.replace("*/", "COMMENT_STAR_DASH")
body = fix_operators(body, ">=", "LOQ")
body = fix_operators(body, "==", "EQUAL")
body = fix_operators(body, "<=", "GOQ")
body = fix_operators(body, "!=", "NOT_EQUAL")
body = fix_operators(body, "=", "ASSIGN_VALUE")
body = fix_operators(body, "+", "ADD_VALUES")
body = fix_operators(body, "-", "SUBTRACT_VALUES")
body = fix_operators(body, "*", "MULTIPLY_VALUES")
body = fix_operators(body, "/", "DIVIDE_VALUES")
body = fix_operators(body, ":", "ARRAY_SYMBOL")
body = fix_operators(body, "||", "BOOLEAN_OR")
body = body.replace("\t BOOLEAN_OR", "\tBOOLEAN_OR")
body = fix_operators(body, "&&", "BOOLEAN_AND")
body = body.replace("\t BOOLEAN_AND", "\tBOOLEAN_AND")
body = body.replace("> ", ">")
body = body.replace(">", "> ")
body = body.replace("> (", ">(")
body = body.replace("> >", ">>")
body = body.replace(", ", ",")
body = body.replace(",", ", ")
body = body.replace("string ", "String ")
body = body.replace("system", "System")
body = body.replace("set<", "Set<")
body = body.replace("set <", "Set<")
body = body.replace("list <", "List<")
body = body.replace("list<", "List<")
body = body.replace("test", "Test")
body = body.replace("@istest", "@isTest")
body = body.replace("select", "SELECT")
body = body.replace("from", "FROM")
body = body.replace("From", "FROM")
body = body.replace("where", "WHERE")
body = body.replace("Where", "WHERE")
body = body.replace("in", "IN")
body = body.replace("In", "IN")
body = body.replace("If", "if")
body = body.replace("IF", "if")
body = body.replace("INsert", "insert")
body = body.replace("Insert", "insert")
body = body.replace("INSERT", "insert")
body = body.replace("UPdate", "update")
body = body.replace("Update", "update")
body = body.replace("UPDATE", "update")
body = body.replace("DElete", "delete")
body = body.replace("Delete", "delete")
body = body.replace("DELETE", "delete")
body = body.replace("for(", "for (")
body = body.replace("if(", "if (")
body = body.replace("else{", "else {")
body = body.replace("){", ") {")
body = body.replace(")>", ") >")
body = body.replace(")<", ") <")

for i in range(1, 10):
    body = body.replace(")\n" + (i * "\t") + "{", ") {")
    body = body.replace("else\n" + (i * "\t") + "{", "else {")

body = body.replace("static TestMethod", "@isTest\n\tstatic")
body = body.replace("COMMENT_DASH_DASH", "//")
body = body.replace("COMMENT_DASH_STAR", "/*")
body = body.replace("COMMENT_STAR_DASH", "*/")
body = body.replace("LOQ", ">=")
body = body.replace("EQUAL", "==")
body = body.replace("GOQ", "<=")
body = body.replace("NOT_EQUAL", "!=")
body = body.replace("ASSIGN_VALUE", "=")
body = body.replace("ADD_VALUES", "+")
body = body.replace("SUBTRACT_VALUES", "-")
body = body.replace("MULTIPLY_VALUES", "*")
body = body.replace("DIVIDE_VALUES", "/")
body = body.replace("ARRAY_SYMBOL", ":")
body = body.replace("BOOLEAN_OR", "||")
body = body.replace("BOOLEAN_AND", "&&")

new_f.write(body)
new_f.close()