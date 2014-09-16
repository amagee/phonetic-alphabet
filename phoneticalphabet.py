import itertools
import jinja2

words = [l.strip() for l in open("/usr/share/dict/words").readlines()]
words = [w for w in words if w and not w.endswith("'s")]
words.sort(key=lambda w: w.lower())

letters = []
for letter, l_words in itertools.groupby(words, lambda w: w[0].lower()):
    longest_word = sorted(list(l_words), key=len)[-1]
    letters.append((letter, longest_word))

template = """
<!DOCTYPE html>
<html>
    <body>
        <h1>Phonetic Alphabet</h1>

        <table>
            {% for i in rows %}
                <tr>
                    {% for j in cols %}
                        <td>
                            {{ cell(i, j) }}
                        </td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </table>
    </body>
</html>
"""

def cell(r, c):
    l = letters[c * 13 + r]
    return "{}: {}".format(l[0], l[1])

t = jinja2.Environment().from_string(template)
print(t.render(rows=range(0, 13), cols=range(0, 2), cell=cell))
    


