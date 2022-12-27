class QueryError(Exception):
    def __init__(self, errors, query = None):
        msg = ""
        for e in errors:
            pos = []
            for p in e["locations"]:
                pos.append("%d:%d" % (p["line"], p["column"]))
            
            msg += "At %s : %s" % (",".join(pos), e["message"])
        
        self.query = query

        msg += "\n" + query

        super().__init__(msg)

class NodeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)