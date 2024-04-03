import json
import glob

output_html = 'index.html'

with open(output_html, 'w') as md_file:
    part = '''
                <head>
                    <title>Perception to Action</title>
                </head>
                <body>
                <h2> Abstract</h2>
                <p> Providing a user-friendly interface for the operators of 
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
                complicated tasks with minimum effort.</p>

                <video width="320" height="240" controls loop="" autoplay="" muted ="">
                    <source src="./assets/SGGLLM.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>

            '''
        

    md_file.write(part)
    exp_type = [['c','Clear'],['a','Abstract'],['f','Fuzzy']]
    for exp in exp_type:
        md_file.write(f"<h2> {exp[1]} Prompts</h2>\n")
        num_exps = len(glob.glob(f'expirements/{exp[0]}/*'))
        for i in range(1,num_exps+1):
            md_file.write(f"<h3> Scenario {i}</h3>\n")
            with open(f'expirements/{exp[0]}/{i}/commands.json') as json_file:
                data = json.load(json_file)
            md_file.write(f"<strong>Prompt:<strong> \n> <blockquote> {data['prompt']} </blockquote>\n")
            md_file.write(f"\n")


            md_file.write(f"<strong>LLM Explanation:</strong> \n> <p>{data['explanation']}</p>\n")

            md_file.write(f"\n")
            md_file.write(f"<strong>LLM Commands:</strong> \n")
            md_file.write(f"<ul>\n")
            for command in data['commands']:
                fn = command['function'].replace('_',' ')
                obg = command['object'].replace('_',' ')
                if obg == '':
                    md_file.write(f"<li> {fn} </li>\n")
                else:
                    md_file.write(f"<li> {fn} -> {obg}</li>\n")
            
 
            
            md_file.write(f"</ul>\n")
            md_file.write(f"<strong>Preview</strong> \n")
            md_file.write(f"\n")

            md_file.write(f'<img src="./expirements/{exp[0]}/{i}/exp.gif" alt="Preview" />\n')
    part = '''
            <h2>Authors</h2>
            <ul>
                <li> Christos Chronis Ph.D. Candidate </li>
                <li> Iraklis Varlamis, Professor </li>
                <li> Dimitrios Michail, Associate Professor </li>
                <li> Konstantinos Tserpes, Associate Professor </li>
                <li> Georgios Dimitrakopoulos, Associate Professor </li>
            </ul>
            </body>
            ''' 




