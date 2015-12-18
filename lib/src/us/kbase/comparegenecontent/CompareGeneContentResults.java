
package us.kbase.comparegenecontent;

import java.util.HashMap;
import java.util.List;
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
    "genes_in_common"
})
public class CompareGeneContentResults {

    @JsonProperty("genes_in_common")
    private List<String> genesInCommon;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("genes_in_common")
    public List<String> getGenesInCommon() {
        return genesInCommon;
    }

    @JsonProperty("genes_in_common")
    public void setGenesInCommon(List<String> genesInCommon) {
        this.genesInCommon = genesInCommon;
    }

    public CompareGeneContentResults withGenesInCommon(List<String> genesInCommon) {
        this.genesInCommon = genesInCommon;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((("CompareGeneContentResults"+" [genesInCommon=")+ genesInCommon)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
