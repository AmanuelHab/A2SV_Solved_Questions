class Solution(object):
    def subdomainVisits(self, cpdomains):
        # extract numbers and domains and store it into dictionary
        cpd_dict = defaultdict(int)
        for paired_domain in cpdomains:
            first_space = paired_domain.find(" ")
            count = int(paired_domain[:first_space])
            domain = paired_domain[first_space + 1:]
            cpd_dict[domain] += count
        # Do the math
        for key, value in cpd_dict.items():
            dot1 = key.find(".")
            if dot1 != -1:
                domain = key[dot1 + 1:]
                cpd_dict[domain] += value
                
                #Find dot2
                dot2 = key.find(".", dot1 + 1)
                if dot2 != -1:
                    higher_domain = key[dot2 + 1: ]
                    cpd_dict[higher_domain] += value
        answer = []
        for key, value in cpd_dict.items():
            answer.append("{} {}".format(value, key))

        return answer
