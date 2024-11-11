package test

import (
    "testing"
    "github.com/gruntwork-io/terratest/modules/terraform"
    "github.com/stretchr/testify/assert"
)

func TestTerraformSecurityHub(t *testing.T) {
    terraformOptions := &terraform.Options{
        TerraformDir: "../../terraform",
        Vars: map[string]interface{}{
            "environment": "test",
        },
    }

    defer terraform.Destroy(t, terraformOptions)
    terraform.InitAndApply(t, terraformOptions)

    securityHubEnabled := terraform.Output(t, terraformOptions, "security_hub_enabled")
    assert.NotEmpty(t, securityHubEnabled)
}
