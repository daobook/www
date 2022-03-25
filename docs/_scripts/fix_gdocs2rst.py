# Script used to migrate gdocs into RST. 
# Historically used for the salary survey, but might be useful otherwise. 
in_rubric = False


with open('survey.rst') as fp:
    for line in fp:
               #print("Line {}: {}".format(cnt, line))

        if line == "+-----------------------------------------------------------------------+\n" and not in_rubric:
            in_rubric = True
        elif in_rubric and line.startswith('| .. rubric:: '):
          #line = ".. container:: "+line[14:-2]
          print(".. container:: question")
        elif in_rubric and line.startswith('|    :'):
          line = line[2:-2]
          #print(line)
        elif (
            line
            == "+-----------------------------------------------------------------------+\n"
        ):
            in_rubric = False
        elif in_rubric:
            line = f"   {line[2:-2]}"
            print(line)
        else:
            print(line, end="")
         
