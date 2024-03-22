import json
import glob

output_markdown = 'README.md'

with open(output_markdown, 'w') as md_file:
    md_file.write(f"# Perception to Action\n")
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
         




