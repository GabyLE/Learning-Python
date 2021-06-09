import xml.etree.ElementTree as ET
count = list()
input = '''
<commentinfo>
<note>This file contains the sample data for testing</note>
<comments>
<comment>
<name>Romina</name>
<count>97</count>
</comment>
<comment>
<name>Laurie</name>
<count>97</count>
</comment>
<comment>
<name>Bayli</name>
<count>90</count>
</comment>
<comment>
<name>Siyona</name>
<count>90</count>
</comment>
<comment>
<name>Taisha</name>
<count>88</count>
</comment>
<comment>
<name>Alanda</name>
<count>87</count>
</comment>
<comment>
<name>Ameelia</name>
<count>87</count>
</comment>
<comment>
<name>Prasheeta</name>
<count>80</count>
</comment>
<comment>
<name>Asif</name>
<count>79</count>
</comment>
<comment>
<name>Risa</name>
<count>79</count>
</comment>
<comment>
<name>Zi</name>
<count>78</count>
</comment>
<comment>
<name>Danyil</name>
<count>76</count>
</comment>
<comment>
<name>Ediomi</name>
<count>76</count>
</comment>
<comment>
<name>Barry</name>
<count>72</count>
</comment>
<comment>
<name>Lance</name>
<count>72</count>
</comment>
<comment>
<name>Hattie</name>
<count>66</count>
</comment>
<comment>
<name>Mathu</name>
<count>66</count>
</comment>
<comment>
<name>Bowie</name>
<count>65</count>
</comment>
<comment>
<name>Samara</name>
<count>65</count>
</comment>
<comment>
<name>Uchenna</name>
<count>64</count>
</comment>
<comment>
<name>Shauni</name>
<count>61</count>
</comment>
<comment>
<name>Georgia</name>
<count>61</count>
</comment>
<comment>
<name>Rivan</name>
<count>59</count>
</comment>
<comment>
<name>Kenan</name>
<count>58</count>
</comment>
<comment>
<name>Hassan</name>
<count>57</count>
</comment>
<comment>
<name>Isma</name>
<count>57</count>
</comment>
<comment>
<name>Samanthalee</name>
<count>54</count>
</comment>
<comment>
<name>Alexa</name>
<count>51</count>
</comment>
<comment>
<name>Caine</name>
<count>49</count>
</comment>
<comment>
<name>Grady</name>
<count>47</count>
</comment>
<comment>
<name>Anne</name>
<count>40</count>
</comment>
<comment>
<name>Rihan</name>
<count>38</count>
</comment>
<comment>
<name>Alexei</name>
<count>37</count>
</comment>
<comment>
<name>Indie</name>
<count>36</count>
</comment>
<comment>
<name>Rhuairidh</name>
<count>36</count>
</comment>
<comment>
<name>Annoushka</name>
<count>32</count>
</comment>
<comment>
<name>Kenzi</name>
<count>25</count>
</comment>
<comment>
<name>Shahd</name>
<count>24</count>
</comment>
<comment>
<name>Irvine</name>
<count>22</count>
</comment>
<comment>
<name>Carys</name>
<count>21</count>
</comment>
<comment>
<name>Skye</name>
<count>19</count>
</comment>
<comment>
<name>Atiya</name>
<count>18</count>
</comment>
<comment>
<name>Rohan</name>
<count>18</count>
</comment>
<comment>
<name>Nuala</name>
<count>14</count>
</comment>
<comment>
<name>Maram</name>
<count>12</count>
</comment>
<comment>
<name>Carlo</name>
<count>12</count>
</comment>
<comment>
<name>Japleen</name>
<count>9</count>
</comment>
<comment>
<name>Breeanna</name>
<count>7</count>
</comment>
<comment>
<name>Zaaine</name>
<count>3</count>
</comment>
<comment>
<name>Inika</name>
<count>2</count>
</comment>
</comments>
</commentinfo>'''

stuff = ET.fromstring(input) #lee el string
lst = stuff.findall('comments/comment')#acomoda las etiquetas en una lista. una lista de mini arboles
print('User count:', len(lst))

for item in lst: #loop within the list of tags
    #print('Name', item.find('name').text)
    count.append(int(item.find('count').text))
    #print('Attribute', item.get('x'))
print(sum(count))