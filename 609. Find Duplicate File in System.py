class Solution(object):
    def findDuplicate(self, paths):
        content_dir = defaultdict(list)
        for path in paths:
            path = path.split()
            dir = path[0]
            files = path[1:]
            for fille in files:
                open_b = fille.find("(")
                content = fille[open_b + 1: -1]
                this_dir = dir + '/' + fille[:open_b]
                content_dir[content].append(this_dir)
        answer = []
        for content, dirs in content_dir.items():
            if len(dirs) > 1:
                answer.append(dirs)
        return answer
