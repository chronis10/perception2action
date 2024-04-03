import json
import glob

output_markdown = 'README.md'

with open(output_markdown, 'w') as md_file:

    md_file.write(f"# Perception to Action\n")
    part1 = '''## Abstract \n Providing a user-friendly interface for the operators of 
            robotic devices is challenging but can save them precious time when
            reprogramming a device to perform different tasks under varying conditions. 
            This paper presents a novel pipeline that adds context awareness at every 
            step of the task execution and employs LLMs to develop a textual interface 
            that supports commands and directions in natural language. Contextual 
            awareness is achieved by analysing input from a camera that supervises 
            the task execution and leveraging 6D pose estimation and scene graph 
            generation models, to create an enriched representation of the task's 
            environment. The rich scene graph incorporates spatial information and 
            refined relationships between objects, and along with the user prompt in 
            natural language is given as input to an LLM-powered chatbot, thus 
            enabling a more intuitive interaction between the user and the robot that 
            requires the minimum information from the user. The first experiments in a 
            simulated environment demonstrate the effectiveness of the proposed approach 
            in facilitating task execution through natural language inputs, empowering 
            users without programming expertise to interact seamlessly with robotic systems and achieve 
            complicated tasks with minimum effort.\n'''
    
    md_file.write(part1)
    exp_type = [['c','Clear'],['a','Abstract'],['f','Fuzzy']]
    for exp in exp_type:
        md_file.write(f"## {exp[1]} Prompts\n")
        num_exps = len(glob.glob(f'expirements/{exp[0]}/*'))
        for i in range(1,num_exps+1):
            md_file.write(f"## Scenario {i}\n")
            with open(f'expirements/{exp[0]}/{i}/commands.json') as json_file:
                data = json.load(json_file)
            md_file.write(f"**Prompt** \n> {data['prompt']}\n")
            md_file.write(f"\n")


            md_file.write(f"**LLM Explanation** \n> {data['explanation']}\n")

            md_file.write(f"\n")
            md_file.write(f"**LLM Commands** \n")
            md_file.write(f"\n")
            for command in data['commands']:
                fn = command['function'].replace('_',' ')
                obg = command['object'].replace('_',' ')
                if obg == '':
                    md_file.write(f"* {fn}\n")
                else:
                    md_file.write(f"* {fn} -> {obg}\n")
 
            
            md_file.write(f"\n")
            md_file.write(f"**Preview** \n")
            md_file.write(f"\n")
            md_file.write(f"![Preview](./expirements/{exp[0]}/{i}/exp.gif)\n")
         




