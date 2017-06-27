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


def generate_naved_template(left_link_names, right_link_names, item_number, checker, site_name = "WRITE-SITE-NAME-HERE!"):
                # file_name = 'output_template.html'

              combined_link_names = left_link_names + right_link_names

              context = {
                                'left_link_names' : left_link_names,
                                'right_link_names' : right_link_names,
                                'site_name' : site_name,
                                'item_number' : item_number,
                                'left_list_size' : len(left_link_names),
                                'right_link_index' : ((item_number) - len(left_link_names) ),
                                'combined_link_names' : combined_link_names,
                                'checker' : checker,

                          }




              html = render('nav-bar.html', context) #eikhane continue korba
              return(html)



def html_file_maker(html, name):
    file_name = name + ".html"
    file = open(file_name,'w')
    file.write(html)
    file.close()


def generate_template_package(left_link_names, right_link_names, site_name= "Ass Fart!"):
    combined_list = left_link_names + right_link_names


    for item in range(len(combined_list)):
        if (item >= len(left_link_names)):
            checker = True
        else:
            checker = False
        html = generate_naved_template(left_link_names, right_link_names, checker=checker, item_number= item, site_name= "Ass Fart!")
        html_file_maker(html, combined_list[item])



def main():
        create_index_html()

########################################

# eita lagbe - uncomment on final edition
# if __name__ == "__main__":
#     main()


left_link_names = ['Home', 'Link 1', 'Link 2']
right_link_names = ['About Us', 'Log In', 'Sign Up']

# html = generate_naved_template(left_link_names, right_link_names, item_number= 0, site_name= "Ass Fart!")
#
#
#
# # Added to write  it works!!
#
# # file = open('testfile.txt','w')
# #
# # file.write(html)
# #
# #
# # file.close()
# html_file_maker(html, "index")


# print(html)

generate_template_package(left_link_names, right_link_names, site_name= "Ass Fart!")

print("Done!")
