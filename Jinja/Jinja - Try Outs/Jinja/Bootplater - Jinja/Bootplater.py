import os
from jinja2 import Environment, FileSystemLoader

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    # loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    loader = FileSystemLoader(os.path.join(PATH)),
    trim_blocks=False)


def render_template(template_filename, context):
        return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)



def render(template_path, context):
        path, filename = os.path.split(template_path)
        return Environment(
            loader= FileSystemLoader(path or './')
        ).get_template(filename).render(context)


def create_index_html():
        fname = "output.html"
        urls = ['http://example.com/1', 'http://example.com/2', 'http://example.com/3']
        context = {
            'urls': urls
        }
        #
        with open(fname, 'w') as f:
            html = render_template('index.html', context)
            f.write(html)


def generate_naved_templates(left_link_names, right_link_names, site_name = "WRITE-SITE-NAME-HERE!"):
                # file_name = 'output_template.html'

              context = {
                                'left_link_names' : left_link_names,
                                'right_link_names' : right_link_names,
                                'site_name' : site_name,
                          }


              html = render('nav-bar.html', context) #eikhane continue korba
              return(html)


def main():
        create_index_html()

########################################

# eita lagbe - uncomment on final edition
# if __name__ == "__main__":
#     main()


left_link_names = ['pizza', 'chiken', 'black thang']
right_link_names = ['sax', 'wax', 'plax', 'max']

html = generate_naved_templates(left_link_names, right_link_names, "Ass Fart!")



# Added to write  it works!!
# file = open('testfile.txt','w')
#
# file.write(html)
#
#
# file.close()

print(html)
