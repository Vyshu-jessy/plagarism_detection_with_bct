// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PlagiarismChecker {
    mapping(string => bool) public submittedHashes;

    function submitDocument(string memory docHash) public {
        require(!submittedHashes[docHash], "Document already submitted!");
        submittedHashes[docHash] = true;
    }

    function checkDocument(string memory docHash) public view returns (bool) {
        return submittedHashes[docHash];
    }
}
