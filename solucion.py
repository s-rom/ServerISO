#!/usr/bin/python3
import re
import os
from colorama import Fore


sol_pattern = re.compile("(?:[sS]olu[ct]i[oó]n):\s*(.*)")
ex_pattern = re.compile("(\d)\)(.*)")

def parse_and_solve(sol_file_path):
    solutions = []
    current_sol = -1

    with open(sol_file_path, 'r') as sol_file:
        for line in sol_file:

            solution=None
            exercise=None


            match = ex_pattern.match(line)
            if match != None:
                current_sol += 1
                solutions.append({"statement": match.group(2), "number": match.group(1)})

            match = sol_pattern.match(line)
            if match != None:
                expected_output=os.popen(match.group(1)).read()
                solutions[current_sol]["expected"] = expected_output
                solutions[current_sol]["solution"] = match.group(1)

    # for sol in solutions:
    #     if "expected" not in sol:
    #         print("Error: No se encuentra la solución para el ejercicio {} en el fichero {}"
    #             .format(sol["number"], sol_file_path))


    return solutions            

def compare_solutions(sol_file_path, ex_file_path):

    student_solutions = parse_and_solve(ex_file_path)
    reference_solutions = parse_and_solve(sol_file_path)

    for i in range(len(reference_solutions)):
        student_sol = student_solutions[i]
        ref_sol = reference_solutions[i]

        print("{}************{} EJERCICIO {} {} ************{}"
            .format(Fore.BLUE, Fore.WHITE, student_sol["number"], Fore.BLUE, Fore.WHITE))
        #print(Fore.WHITE + "[Enunciado]: {}".format(student_sol["statement"]))

        


        if "expected" not in student_sol:
            print(Fore.RED + " ==> Error! No has dado solución a este ejercicio\n" + Fore.WHITE)
            continue 
        
        print("[Tu solución]: {}".format(student_sol["solution"]))

        if (student_sol["expected"] != ref_sol["expected"]):
            print(Fore.RED + "\n   ------> Resultado esperado <------{}\n{}"
                .format(Fore.WHITE, ref_sol["expected"]) + Fore.WHITE)
            print("   ------> Resultado de tu solución <------\n{}".format(student_sol["expected"]))
        else:
            print(Fore.GREEN  + "Correcto!" + Fore.WHITE)


        print()




exercise = os.path.basename(os.getcwd())
sol_file_path="/.secret/{}.txt".format(exercise)
ex_file_path="./"+exercise+".txt"


compare_solutions(sol_file_path, ex_file_path)
     
