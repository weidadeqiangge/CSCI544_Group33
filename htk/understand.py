#!/usr/bin/env python3

monthname = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];
cardinal1 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
cardinal10 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
cardinal20 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
ordinal1 = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth"];
ordinal10 = ["tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth"];
ordinal20 = ["twentieth", "thirtieth", "fortieth", "fiftieth", "sixtieth", "seventieth", "eightieth", "ninetieth"];

yes_words = ["yes", "yeah", "right", "correct", "confirm"];
no_words = ["no"];

# --------------------------------------------------------------------

def read_name(words, index, predicates):
	start = index;
	stop = len(words);
	non_name_words = ["to", "on", "and", "while", "but", "departing", "leaving", "i", "want", "my", "the", "be", "do", "see", "look", "eat"];
	non_name_words += monthname + cardinal1 + cardinal10 + cardinal20 + ordinal1 + ordinal10 + ordinal20 + yes_words + no_words;
	for word in words[start:]:
		if word in non_name_words:
			stop = words[start:].index(word) + start;
			break;

	if start == stop:
		return None;

	name = "";
	for word_in_name in words[start:stop]:
		name += " " + word_in_name;
	name = name[1:];
	return name;

def read_origin(words, index, predicates):
	city = read_name(words, index, predicates);
	if city != None:
		predicates.append(("=", "OriginCity", city));
		return True;
	else:
		return False;

def read_destination(words, index, predicates):
	city = read_name(words, index, predicates);
	if city != None:
		predicates.append(("=", "DestinationCity", city));
		return True;
	else:
		return False;

def read_personname(words, index, predicates):
	name = read_name(words, index, predicates);
	if name != None:
		predicates.append(("=", "MyName", name));
		return True;
	else:
		return False;

# --------------------------------------------------------------------

def read_month(words, i, predicates):
	if words[i] in monthname:
		return monthname.index(words[i])+1;
	return None;

def read_date(words, i, predicates):
	if words[i] in cardinal20:
		if i+1<len(words) and words[i+1] in ordinal1: # This should be a start of a date
			return cardinal20.index(words[i])*10+20 + ordinal1.index(words[i+1])+1;
	if words[i] in ordinal20: # This should be a date of 20th or 30th
		return ordinal20.index(words[i])*10+20;
	if words[i] in ordinal1+ordinal10: # This should be a date of 1 ~ 19
		return (ordinal1+ordinal10).index(words[i])+1;
	return None;

def read_year(words, i, predicates):
	if i+4<len(words) and words[i:i+3]==["two", "thousand", "and"] and words[i+3] in cardinal20 and words[i+4] in cardinal1:
		return 2000 + cardinal20.index(words[i+3])*10+20 + cardinal1.index(words[i+4])+1;
	if i+3<len(words) and words[i:i+3]==["two", "thousand", "and"] and words[i+3] in cardinal20:
		return 2000 + cardinal20.index(words[i+3])*10+20;
	if i+3<len(words) and words[i:i+3]==["two", "thousand", "and"] and words[i+3] in cardinal1+cardinal10:
		return 2000 + (cardinal1+cardinal10).index(words[i+3])+1;
	if i+3<len(words) and words[i:i+2]==["two", "thousand"] and words[i+2] in cardinal20 and words[i+3] in cardinal1:
		return 2000 + cardinal20.index(words[i+2])*10+20 + cardinal1.index(words[i+3])+1;
	if i+2<len(words) and words[i:i+2]==["two", "thousand"] and words[i+2] in cardinal20:
		return 2000 + cardinal20.index(words[i+2])*10+20;
	if i+2<len(words) and words[i:i+2]==["two", "thousand"] and words[i+2] in cardinal+cardinal10:
		return 2000 + (cardinal1+cardinal10).index(words[i+2])+1;
	if words[i] == "twenty": # Possibly a year number
		if i+2<len(words) and words[i+1] in cardinal20 and words[i+2] in cardinal1:
			return 2000 + cardinal20.index(words[i+1])*10+20 + cardinal1.index(words[i+2])+1;
		if i+1<len(words) and words[i+1] in cardinal20:
			return 2000 + cardinal20.index(words[i+1])*10+20;
		if i+1<len(words) and words[i+1] in cardinal10:
			return 2000 + cardinal10.index(words[i+1])+10;
		if i+2<len(words) and words[i+1]=="oh" and words[i+2] in cardinal1:
			return 2000 + cardinal1.index(words[i+2])+1;
	return None;

def read_month_date_year(words, i, predicates):
	if i==0:
		prefix = "";
	elif i==1 and words[0]=="on":
		prefix = "";
	elif "return" in words[max(i-6,0):i]:
		prefix = "Ret";
	elif "returning" in words[max(i-6,0):i]:
		prefix = "Ret";
	else:
		prefix = "Out";

	month = read_month(words, i, predicates);
	if month == None:
		return False;
	if i+1<len(words) and words[i+1] == "the":
		if i+2<len(words):
			date = read_date(words, i+2, predicates);
		else:
			date = None;
	else:
		if i+1<len(words):
			date = read_date(words, i+1, predicates);
		else:
			date = None;
	if date == None:
		return False;
	predicates.append(("=", prefix + "DepartureTimeMonth", month));
	predicates.append(("=", prefix + "DepartureTimeDate", date));

	if i+1<len(words) and words[i+1] == "the":
		if date > 20 and date%10!=0:
			if i+4<len(words):
				year = read_year(words, i+4, predicates);
			else:
				year = None;
		else:
			if i+3<len(words):
				year = read_year(words, i+3, predicates);
			else:
				year = None;
	else:
		if date > 20 and date%10!=0:
			if i+3<len(words):
				year = read_year(words, i+3, predicates);
			else:
				year = None;
		else:
			if i+2<len(words):
				year = read_year(words, i+2, predicates);
			else:
				year = None;
	if year != None:
		predicates.append(("=", prefix + "DepartureTimeYear", year));
	return True;

# --------------------------------------------------------------------

def understand(utterance):
	words = utterance.lower().split();
	predicates = []

	for i in range(len(words)):
		if words[i] in yes_words:
			predicates.append(("True",));
			continue;
		if words[i] in no_words:
			predicates.append(("False",));
			continue;

		if i+1<len(words) and words[i:i+2]==["economy", "class"]:
			predicates.append(("=", "Class", "Economy"));
			continue;
		if i+1<len(words) and words[i:i+2]==["business", "class"]:
			predicates.append(("=", "Class", "Business"));
			continue;
		if i+1<len(words) and words[i:i+2]==["first", "class"]:
			predicates.append(("=", "Class", "First"));
			continue;

		if words[i]=="roundtrip":
			predicates.append(("=", "RoundTrip", "True"));
			continue;
		if i+2<len(words) and words[i:i+3]==["one", "way", "trip"]:
			predicates.append(("=", "RoundTrip", "False"));
			continue;

		if read_month_date_year(words, i, predicates):
			continue;

		if i==0:
			if read_personname(words, i, predicates):
				continue;
		if i==1 and words[0] in yes_words+no_words:
			if read_personname(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["name", "is"]:
			if read_personname(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["name", "to"]:
			if read_personname(words, i, predicates):
				continue;

		if i>=1 and words[i-1] == "from":
			if read_origin(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["source", "is"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["origin", "is"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["source", "to"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["origin", "to"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["source", "city", "is"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["origin", "city", "is"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["source", "city", "to"]:
			if read_origin(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["origin", "city", "to"]:
			if read_origin(words, i, predicates):
				continue;

		if i>=2 and words[i-2:i]==["destination", "is"]:
			if read_destination(words, i, predicates):
				continue;
		if i>=2 and words[i-2:i]==["destination", "to"]:
			if read_destination(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["destination", "city", "is"]:
			if read_destination(words, i, predicates):
				continue;
		if i>=3 and words[i-3:i]==["destination", "city", "to"]:
			if read_destination(words, i, predicates):
				continue;
		if i>=1 and words[i-1] == "to" and not (i>=2 and words[i-2] in ["want"]):
			if read_destination(words, i, predicates):
				continue;

	return predicates;


utterance = input();
print(understand(utterance));
