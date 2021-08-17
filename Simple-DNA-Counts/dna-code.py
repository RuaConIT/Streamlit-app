from altair.vegalite.v4.schema.channels import Column
from altair.vegalite.v4.schema.core import Header
import pandas as pd 
from PIL import Image
from requests.api import head
import streamlit as st
import altair as alt

image = Image.open('dna-logo.jpg')
st.image(image, use_column_width=True)

st.write("""
    # DNA Count Web APP
    This app counts the nucleotide composition of query DNA ! 
    ***

""")

st.header('Enter DNA Senquence')
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ''.join(sequence)

st.header('Input (DNA Query)')
sequence

st.header('Output (DNA Nucleotide Count)')
st.subheader('1. Print dictionary')
def DNA_Count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
        ('T', seq.count('T')),
    ])
    return d

P = DNA_Count(sequence)
P

st.subheader('2. Print Text')
st.write('There are ' + str(P['A']) + ' adenine (A)')
st.write('There are ' + str(P['G']) + ' guanine (G)')
st.write('There are ' + str(P['T']) + ' thymine (T)')
st.write('There are ' + str(P['C']) + ' cytosine (C)')

st.subheader('3. Display Dataframe')
df = pd.DataFrame.from_dict(P, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(x = 'nucleotide', y = 'count')
p = p.properties(width=alt.Step(80))
st.write(p)