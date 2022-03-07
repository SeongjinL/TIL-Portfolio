class Query:
    keyword = "none"
    hashtag = "none"
    is_retweet = False

    def __init__(self, keyword, hashtag, is_retweet) :
        self.keword = keyword
        self.hashtag = hashtag
        self.is_retweet = is_retweet
        return

    def __str__(self):
        query_str = ""
        if self.keword != "none" :
            query_str += "\""+self.keword+"\" "
        if self.hashtag != "none" :
            query_str += self.hashtag+" "
        if self.is_retweet == True:
            query_str += "is:retweet"
        else :
            query_str += "-is:retweet"
        return query_str


            

        
        