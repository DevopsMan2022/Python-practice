def name_awscert(name: str, certificate_name: str) -> str:
    """
    This code will take 2 inpuits
    1. name --> string
    2. AWS certificate name --> string
    output will be combination of both the inputs
    """
    result = name + ' is' + ' AWS certified ' + certificate_name
    return result

def pod_name(pod_name: str) -> str:
    """
    This method will take 1 input
    pod_name it should be string 
    output will be like pod: pod_name and its a string
    """
    return "Pod:" + pod_name

def eks_cluster_name_length(cluster_name : str) ->str:
    if(len(cluster_name)>5):
        return 'cluster name is greater than 5 letters'
    else:
        return 'cluster name is not greater than 5 letters'


def main():
    print(name_awscert('Manohar' , 'Solution Architect Associate'))
    print(pod_name('openresty_nginx'))
    # print(sum_state(10, -10))
    print(eks_cluster_name_length('cp-test-ekscluster'))

if __name__ == '__main__':
    main()