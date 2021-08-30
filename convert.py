# SYNTAX: python convert.py <file 1 name> <file 2 name> ... <file n name>
import sys

for f_name in sys.argv[1:]:
    try:
        f = open(f_name, "r+")
    except FileNotFoundError:
        print("\033[1;31;40mFile does not exist: " + f_name)
        continue


    def fix_operators(text, operator, operator_name):
        text = text.replace(operator, operator_name)
        text = text.replace(operator_name + " ", operator_name)
        text = text.replace(" " + operator_name, operator_name)
        text = text.replace(" " + operator_name + " ", operator_name)
        text = text.replace(operator_name, " " + operator_name + " ")
        return text


    # MANAGE FILES
    body = f.read()
    f.close()
    f = open(f_name, "w")
    f_name_array = f_name.split(".")
    try:
        f_backup = open(f_name_array[0] + "_old." + f_name_array[1], "w")
    except IndexError:
        f_backup = open(f_name + ".old", "w")
    f_backup.write(body)
    f_backup.close()

    # SPACING
    body = body.replace("    ", "\t")  # change 4 spaces to one tab
    body = body.replace("   ", "\t")  # change 3 spaces to one tab to fix spacing
    body = body.replace("  ", "")  # remove all 2 spaces symbols to fix spacing

    # CHANGE OPERATORS TO WORDS
    body = body.replace("/**", "DOCU_START")
    body = body.replace("**", "DOCU_BODY")
    body = body.replace("**/", "DOCU_END")
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

    # FIX GENERAL PROBLEMS
    body = body.replace("> ", ">")
    body = body.replace(">", "> ")
    body = body.replace("> (", ">(")
    body = body.replace("> >", ">>")
    body = body.replace(", ", ",")
    body = body.replace(",", ", ")
    body = body.replace("string ", "String ")
    body = body.replace("map", "Map")
    body = body.replace("decimal", "Decimal")
    body = body.replace("boolean ", "Boolean ")
    body = body.replace("system", "System")
    body = body.replace("set<", "Set<")
    body = body.replace("set <", "Set<")
    body = body.replace("list <", "List<")
    body = body.replace("list<", "List<")
    body = body.replace("test", "Test")
    body = body.replace("@istest", "@isTest")
    body = body.replace("select", "SELECT")
    body = body.replace("Select", "SELECT")
    body = body.replace("from", "FROM")
    body = body.replace("From", "FROM")
    body = body.replace("where", "WHERE")
    body = body.replace("Where", "WHERE")
    body = body.replace(" Order by ", " ORDER BY ")
    body = body.replace(" Order By ", " ORDER BY ")
    body = body.replace(" order by ", " ORDER BY ")
    body = body.replace(" Desc ", "DESC")
    body = body.replace(" Asc ", " ASC ")
    body = body.replace(" Or ", " OR ")
    body = body.replace(" or ", " OR ")
    body = body.replace(" And ", " AND ")
    body = body.replace(" and ", " AND ")
    body = body.replace("If", "if")
    body = body.replace("IF", "if")
    body = body.replace(" in ", " IN ")
    body = body.replace(" In ", " IN ")
    body = body.replace("id,", "Id,")
    body = body.replace("id>", "Id>")
    body = body.replace("<id", "<Id")
    body = body.replace(".id", ".Id")
    body = body.replace("Insert", "insert")
    body = body.replace("INSERT", "insert")
    body = body.replace("Update", "update")
    body = body.replace("UPDATE", "update")
    body = body.replace("Delete", "delete")
    body = body.replace("DELETE", "delete")
    body = body.replace("for(", "for (")
    body = body.replace("if(", "if (")
    body = body.replace("else{", "else {")
    body = body.replace("){", ") {")
    body = body.replace(")>", ") >")
    body = body.replace(")<", ") <")
    body = body.replace("static TestMethod", "@isTest\n\tstatic")
    body = body.replace("System.UserInfo", "UserInfo")
    body = body.replace("UserInfo", "System.UserInfo")

    for i in range(1, 10):
        body = body.replace(")\n" + (i * "\t") + "{", ") {")
        body = body.replace("else\n" + (i * "\t") + "{", "else {")

    # REVERSE CHANGES OPERATOR => WORD
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
    body = body.replace("DOCU_START", "/**")
    body = body.replace("DOCU_BODY", "**")
    body = body.replace("DOCU_END", "**/")

    f.write(body)
    f.close()

    print("\033[1;32;40mFile: " + f_name + " successfully saved")
