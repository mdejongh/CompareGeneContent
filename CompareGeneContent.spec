/*
A KBase module: CompareGeneContent
This sample module contains one small method - count_contigs.
*/

module CompareGeneContent {
	/*
	A string representing an FBAModel id.
	*/
	typedef string model_id;
	
	/*
	A string representing an ExpressionMatrix id.
	*/
	typedef string matrix_id;
	
	/*
	A string representing a workspace name.
	*/
	typedef string workspace_name;
	
	typedef structure {
	    list<string> genes_in_common;
	} CompareGeneContentResults;
	
	/*
	Compares gene content in FBAModel and ExpressionMatrix
	*/
	funcdef compare_gene_content(workspace_name,model_id,matrix_id) returns (CompareGeneContentResults) authentication required;
};