
package us.kbase.comparegenecontent;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: CompareGeneContentResults</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "gene_intersection_count",
    "matrix_gene_count",
    "model_gene_count"
})
public class CompareGeneContentResults {

    @JsonProperty("gene_intersection_count")
    private Long geneIntersectionCount;
    @JsonProperty("matrix_gene_count")
    private Long matrixGeneCount;
    @JsonProperty("model_gene_count")
    private Long modelGeneCount;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("gene_intersection_count")
    public Long getGeneIntersectionCount() {
        return geneIntersectionCount;
    }

    @JsonProperty("gene_intersection_count")
    public void setGeneIntersectionCount(Long geneIntersectionCount) {
        this.geneIntersectionCount = geneIntersectionCount;
    }

    public CompareGeneContentResults withGeneIntersectionCount(Long geneIntersectionCount) {
        this.geneIntersectionCount = geneIntersectionCount;
        return this;
    }

    @JsonProperty("matrix_gene_count")
    public Long getMatrixGeneCount() {
        return matrixGeneCount;
    }

    @JsonProperty("matrix_gene_count")
    public void setMatrixGeneCount(Long matrixGeneCount) {
        this.matrixGeneCount = matrixGeneCount;
    }

    public CompareGeneContentResults withMatrixGeneCount(Long matrixGeneCount) {
        this.matrixGeneCount = matrixGeneCount;
        return this;
    }

    @JsonProperty("model_gene_count")
    public Long getModelGeneCount() {
        return modelGeneCount;
    }

    @JsonProperty("model_gene_count")
    public void setModelGeneCount(Long modelGeneCount) {
        this.modelGeneCount = modelGeneCount;
    }

    public CompareGeneContentResults withModelGeneCount(Long modelGeneCount) {
        this.modelGeneCount = modelGeneCount;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("CompareGeneContentResults"+" [geneIntersectionCount=")+ geneIntersectionCount)+", matrixGeneCount=")+ matrixGeneCount)+", modelGeneCount=")+ modelGeneCount)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
