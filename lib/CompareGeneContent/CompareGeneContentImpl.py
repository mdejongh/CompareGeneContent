#BEGIN_HEADER
from biokbase.workspace.client import Workspace as workspaceService
#END_HEADER


class CompareGeneContent:
    '''
    Module Name:
    CompareGeneContent

    Module Description:
    A KBase module: CompareGeneContent
This sample module contains one small method - count_contigs.
    '''

    ######## WARNING FOR GEVENT USERS #######
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    #########################################
    #BEGIN_CLASS_HEADER
    workspaceURL = None
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.workspaceURL = config['workspace-url']
        #END_CONSTRUCTOR
        pass

    def compare_gene_content(self, ctx, workspace_name, model_id, matrix_id):
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN compare_gene_content
        token = ctx['token']
        wsClient = workspaceService(self.workspaceURL, token=token)
        model = wsClient.get_objects([{'ref': workspace_name+'/'+model_id}])[0]['data']
        model_genes = []
        for mr in model['modelreactions']:
            for mrp in mr['modelReactionProteins']:
                for mrps in mrp['modelReactionProteinSubunits']:
                    for fr in mrps['feature_refs']:
                        model_genes.append(fr.split('/').pop())
        from pprint import pprint
        pprint(model_genes)
        matrix = wsClient.get_objects([{'ref': workspace_name+'/'+matrix_id}])[0]['data']
        matrix_genes = matrix['data']['row_ids']
        both_genes = list(set(model_genes) & set(matrix_genes))
        returnVal = { 'gene_intersection': both_genes }
        #END compare_gene_content

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method compare_gene_content return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
