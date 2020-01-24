from collections import defaultdict

class DataSet:
    def __init__(self, examples=None, attrs=None, attrnames=None, target=-1,
                 inputs=None, values=None, name='', exclude=()):
        self.examples = examples
        self.name = name
        self.values = values
        self.got_values_flag = bool(values)

        #Attrs are the indices of examples, unless otherwise stated
        if self.examples and not attrs:
            attrs = list(range(len(self.examples[0])))
        self.attrs = attrs

        #Initialize .attrnames from string, list or by default
        if isinstance(attrnames, str):
            self.attrnames = attrnames.split(",")
        else:
            self.attrnames = attrnames or attrs
        self.setproblem(target, inputs=inputs, exclude=exclude)

    def setproblem(self, target, inputs=None, exclude=()):
        self.target = self.attrnum(target)
        exclude = list(map(self.attrnum, exclude))
        if inputs:
            self.inputs = remove_all(self.target, inputs)
        else:
            self.inputs = [a for a in self.attrs
                           if a != self.target and a not in exclude]

    def check_example(self, example):

        if self.values:
            for a in self.attrs:
                if example[a] not in self.values[a]:
                    raise ValueError('Bad values{} for attribute {} in {}'
                                     .format(example[a], self.attrnames[a], example))

    def attrnum(self, attr):
        """Returns the number used for attr, which can be a name, or -n ... n-1"""
        if isinstance(attr, str):
            return self.attrnames.index(attr)
        elif attr < 0:
            return len(self.attrs) + attr
        else:
            return attr

    def sanitize(self, example):
        """Return a copy of example, with non-input attributes replaced by None"""
        return [attr_i if i in self.inputs else None
                for i, attr_i in enumerate(example)]

    def remove_examples(self, value=""):
        """Remove examples that contain given value"""
        self.examples = [x for x in self.examples if value not in x]
        #self.update_values()

    def split_values_by_classes(self):
        """Split values into buckets according to their class."""
        buckets = defaultdict(lambda: [])
        target_names = self.values[self.target]

        for v in self.examples:
            item = [a for a in v if a not in target_names]  #remove target from item
            buckets[v[self.target]].append(item) #Add item to bucket of its class
        return buckets

    def __repr__(self):
        return '<DataSet({}): {:d} examples, {:d} attributes>'.format(
            self.name, len(self.examples), len(self.attrs))


def remove_all(item, seq):
    """Return a copy of seq (or string) with all occurrences of item removed."""
    if isinstance(seq, str):
        return seq.replace(item, '')
    else:
        return [x for x in seq if x != item]