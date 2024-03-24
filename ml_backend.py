from openai import OpenAI

client = OpenAI(api_key='##')

class ml_backend:
        

    def generate_email(self, userPrompt ="Write me a professionally sounding email", start="Dear"):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""
        response = client.completions.create(model="gpt-3.5-turbo-instruct",
            prompt=userPrompt + "\n\n" + start,
            temperature=0.71,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.36,
            presence_penalty=0.75)
        return response.choices[0].text

    def replace_spaces_with_pluses(self, sample):
        """Returns a string with each space being replaced with a plus so the email hyperlink can be formatted properly"""
        changed = list(sample)
        for i, c in enumerate(changed):
            if(c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n'):
                changed[i] = '+'
        return ''.join(changed)
