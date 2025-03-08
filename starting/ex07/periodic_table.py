def generate_css():
    css = """
    body {
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    .element {
        width: 100px;
        height: 150px;
        border: solid 1px;
        margin: 5px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background-color: #f0f0f0;
        border-radius: 5px;
    }
    .element h4 {
        margin: 0;
    }
    .element ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .element ul li {
        margin: 2px 0;
    }
    .small {
        font-size: 2em;
    }
"""
    return css

def generate_case(table):
    new_case = f"""
<div class="element">
    <ul>
        <li class="info">{table["number"]}</li>
        <li class="info">{table["molar"]}</li>
        <li class="small">{table["small"]}</li>
    <h4>{table["name"]}</h4>
    </ul>
</div>
"""
    return new_case

# ##########################################################

def table_creation(content):
    with open("periodic_table.txt") as file:
        for line in file:
            name, data = line.strip().split('=', 1)
            table = {"name": name.strip()}
            data = data.strip().split(', ')
            for item in data:
                key, value = item.split(':')
                table[key.strip()] = value.strip()
            content += generate_case(table)
    return content

# ##########################################################

def html_generator():
    content = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Periodic Table</title>
        <link rel="stylesheet" href="periodic_table.css">
    </head>
    <body>
"""
    content += table_creation("")
    content += """
    </body>
</html>
"""
    css = generate_css()
    with open("periodic_table.css", "w") as style:
        style.write(css)
    with open("periodic_table.html", "w") as doc:
        doc.write(content)

# ##########################################################

if __name__ == '__main__':
    html_generator()